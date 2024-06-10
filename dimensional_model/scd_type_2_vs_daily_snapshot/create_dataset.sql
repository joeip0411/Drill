CREATE DATABASE if not exists practice;

CREATE schema if not exists practice.dimensional_models;

SET customer_sample_size = 1000000;

CREATE
OR REPLACE TEMPORARY TABLE customer_change AS WITH cte AS (
    SELECT
        UNIFORM(1, $customer_sample_size / 2, RANDOM(1)) :: INT AS customer_id,
        MD5(customer_id) AS customer_name,
        RANDSTR(
            UNIFORM(3, 20, RANDOM(4)),
            UNIFORM(5, $customer_sample_size * 4, RANDOM(6))
        ) AS customer_address,
        DATEADD(
            'day',
            FLOOR(UNIFORM(0, 30, RANDOM(7))),
            '2020-01-01'
        ) AS updated_date,
    FROM
        TABLE(GENERATOR(rowcount => $customer_sample_size)) qualify ROW_NUMBER() over (
            PARTITION BY customer_id,
            updated_date
            ORDER BY
                updated_date ASC
        ) = 1 -- one entry per customer per DAY
),
with_row_num AS (
    SELECT
        customer_id,
        customer_name,
        customer_address,
        first_value(updated_date) over(
            PARTITION by customer_id
            ORDER BY
                updated_date ASC
        ) AS registration_date,
        updated_date,
        ROW_NUMBER() over (
            PARTITION BY customer_id
            ORDER BY
                updated_date ASC
        ) AS row_num
    FROM
        cte
)
SELECT
    w1.customer_id,
    w1.customer_name,
    w1.customer_address,
    w1.registration_date,
    w1.updated_date
FROM
    with_row_num w1
    LEFT JOIN with_row_num w2 ON w1.customer_id = w2.customer_id
    AND w1.row_num = w2.row_num -1
WHERE
    w1.customer_address != w2.customer_address
    OR w2.customer_id IS NULL;

CREATE
OR REPLACE TABLE customer_stage AS WITH record_date AS (
    SELECT
        '2019-12-31' :: DATE + n AS record_date
    FROM
        (
            SELECT
                ROW_NUMBER() over(
                    ORDER BY
                        0
                ) n
            FROM
                TABLE(GENERATOR(rowcount => 31))
        )
)
SELECT
    *
FROM
    customer_change C
    JOIN record_date d ON C.updated_date <= d.record_date qualify ROW_NUMBER() over (
        PARTITION BY d.record_date,
        C.customer_id
        ORDER BY
            updated_date DESC
    ) = 1;

SET product_sample_size = 100000;

CREATE
OR REPLACE TEMPORARY TABLE product_change AS WITH cte AS (
    SELECT
        UNIFORM(1, $product_sample_size, RANDOM(1)) :: INT AS product_id,
        MD5(product_id) AS product_name,
        UNIFORM(100, 10000, RANDOM(2)) AS unit_price,
        DATEADD(
            'day',
            FLOOR(UNIFORM(0, 30, RANDOM(3))),
            '2020-01-01'
        ) AS updated_date,
    FROM
        TABLE(GENERATOR(rowcount => $product_sample_size)) qualify ROW_NUMBER() over (
            PARTITION BY product_id,
            updated_date
            ORDER BY
                updated_date ASC
        ) = 1 -- one entry per customer per DAY
),
with_row_num AS (
    SELECT
        product_id,
        product_name,
        unit_price,
        updated_date,
        ROW_NUMBER() over (
            PARTITION BY product_id
            ORDER BY
                updated_date ASC
        ) AS row_num
    FROM
        cte
)
SELECT
    w1.product_id,
    w1.product_name,
    w1.unit_price,
    w1.updated_date
FROM
    with_row_num w1
    LEFT JOIN with_row_num w2 ON w1.product_id = w2.product_id
    AND w1.row_num = w2.row_num -1
WHERE
    w1.unit_price != w2.unit_price
    OR w2.product_id IS NULL;

CREATE
OR REPLACE TABLE product_stage AS WITH record_date AS (
    SELECT
        '2019-12-31' :: DATE + n AS record_date
    FROM
        (
            SELECT
                ROW_NUMBER() over(
                    ORDER BY
                        0
                ) n
            FROM
                TABLE(GENERATOR(rowcount => 31))
        )
)
SELECT
    *
FROM
    product_change C
    JOIN record_date d ON C.updated_date <= d.record_date qualify ROW_NUMBER() over (
        PARTITION BY d.record_date,
        C.product_id
        ORDER BY
            updated_date DESC
    ) = 1;

CREATE
OR REPLACE TABLE order_stage AS WITH cte AS (
    SELECT
        C.customer_id,
        p.product_id,
        MOD(
            C.customer_id + p.product_id,
            10
        ) + 1 AS quantity,
        GREATEST(
            C.updated_date,
            p.updated_date
        ) AS greatest_date
    FROM
        customer_change C,
        product_change p
    WHERE
        C.updated_date > p.updated_date
),
order_sample AS (
    SELECT
        customer_id,
        product_id,
        quantity,
        DATEADD(DAY, UNIFORM(0, 100, RANDOM(8)), greatest_date) AS order_date
    FROM
        cte SAMPLE(4)
),
with_id AS (
    SELECT
        ROW_NUMBER() over (
            ORDER BY
                order_date ASC
        ) AS order_id,
        *
    FROM
        order_sample
)
SELECT
    *
FROM
    with_id;
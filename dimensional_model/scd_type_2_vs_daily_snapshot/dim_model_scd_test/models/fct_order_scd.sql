{{ config(
    materialized ='incremental',
    unique_key = ['order_id']
) }}

SELECT
    o.order_id,
    c.customer_key,
    p.product_key,
    o.quantity,
    o.order_date
FROM
    {{ source('DIMENSIONAL_MODELS','ORDER_STAGE') }} o
    JOIN {{ ref('dim_customer_scd') }} c ON o.customer_id = c.customer_id
    AND c.dbt_valid_from  <= '{{ var('start_date') }}'
    AND (c.dbt_valid_to > '{{ var('start_date') }}' OR c.dbt_valid_to IS NULL)
    JOIN {{ ref('dim_product_scd') }} p ON p.product_id = o.product_id
    AND p.dbt_valid_from  <= '{{ var('start_date') }}'
    AND (p.dbt_valid_to > '{{ var('start_date') }}' OR p.dbt_valid_to IS NULL)
WHERE
    o.order_date >= '{{ var('start_date') }}'
    AND o.order_date < '{{ var('end_date') }}'
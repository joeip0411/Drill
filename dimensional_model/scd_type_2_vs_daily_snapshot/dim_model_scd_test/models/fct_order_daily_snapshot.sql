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
    JOIN {{ ref('dim_customer_daily_snapshot') }} c ON o.customer_id = c.customer_id
    AND c.record_date ='{{ var('start_date') }}'
    JOIN {{ ref('dim_product_daily_snapshot') }} p ON p.product_id = o.product_id
    AND p.record_date ='{{ var('start_date') }}'
WHERE
    o.order_date >= '{{ var('start_date') }}'
    AND o.order_date < '{{ var('end_date') }}'
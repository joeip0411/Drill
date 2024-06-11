{{
    config(
        materialized='incremental',
        unique_key=['product_id', 'record_date']
    )
}}

select 
    {{ dbt_utils.generate_surrogate_key(['product_id', 'record_date']) }} as product_key,
    *
from {{ source('DIMENSIONAL_MODELS', 'PRODUCT_STAGE')}}
where record_date >= '{{ var('start_date') }}'
    and record_date < '{{ var('end_date') }}'
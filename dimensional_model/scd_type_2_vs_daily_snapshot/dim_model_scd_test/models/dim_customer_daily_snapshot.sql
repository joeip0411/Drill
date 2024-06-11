{{
    config(
        materialized='incremental',
        unique_key=['customer_id', 'record_date']
    )
}}

select 
    {{ dbt_utils.generate_surrogate_key(['customer_id', 'record_date']) }} as customer_key,
    *
from {{ source('DIMENSIONAL_MODELS', 'CUSTOMER_STAGE')}}
where record_date >= '{{ var('start_date') }}'
    and record_date < '{{ var('end_date') }}'
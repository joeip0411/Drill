{% snapshot dim_product_scd %}

{{
    config(
      target_database='practice',
      target_schema='dimensional_models',
      unique_key='product_id',
      strategy='timestamp',
      updated_at='updated_date',
    )
}}

select
    {{ dbt_utils.generate_surrogate_key(['product_id', 'record_date']) }} as product_key,
    * 
from {{ source('DIMENSIONAL_MODELS', 'PRODUCT_STAGE') }}
where record_date >= '{{ var('start_date') }}'
    and record_date < '{{ var('end_date') }}'

{% endsnapshot %}
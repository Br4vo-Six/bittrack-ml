## Format transaction (blockcypher)
```
{
    block_height,
    hash,
    addresses,
    total,
    fees,
    size,
    vsize,
    confirmed,
    vin_sz,
    vout_sz,
    inputs: [
        {
            prev_hash,
            output_index,
            output_value,
            addresses,
            script_type,
            age
        },
        ...        
    ],
    outputs: [
        {
            value,
            spent_by,
            addresses,
            script_type
        },
        ...
    ]
}
```
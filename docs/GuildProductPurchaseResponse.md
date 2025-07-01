# GuildProductPurchaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_id** | **str** |  | 
**product_name** | **str** |  | 

## Example

```python
from dc_rest.models.guild_product_purchase_response import GuildProductPurchaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildProductPurchaseResponse from a JSON string
guild_product_purchase_response_instance = GuildProductPurchaseResponse.from_json(json)
# print the JSON string representation of the object
print(GuildProductPurchaseResponse.to_json())

# convert the object into a dict
guild_product_purchase_response_dict = guild_product_purchase_response_instance.to_dict()
# create an instance of GuildProductPurchaseResponse from a dict
guild_product_purchase_response_from_dict = GuildProductPurchaseResponse.from_dict(guild_product_purchase_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



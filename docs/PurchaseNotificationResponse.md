# PurchaseNotificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**guild_product_purchase** | [**GuildProductPurchaseResponse**](GuildProductPurchaseResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.purchase_notification_response import PurchaseNotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseNotificationResponse from a JSON string
purchase_notification_response_instance = PurchaseNotificationResponse.from_json(json)
# print the JSON string representation of the object
print(PurchaseNotificationResponse.to_json())

# convert the object into a dict
purchase_notification_response_dict = purchase_notification_response_instance.to_dict()
# create an instance of PurchaseNotificationResponse from a dict
purchase_notification_response_from_dict = PurchaseNotificationResponse.from_dict(purchase_notification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



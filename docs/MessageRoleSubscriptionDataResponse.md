# MessageRoleSubscriptionDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_subscription_listing_id** | **str** |  | 
**tier_name** | **str** |  | 
**total_months_subscribed** | **int** |  | 
**is_renewal** | **bool** |  | 

## Example

```python
from dc_rest.models.message_role_subscription_data_response import MessageRoleSubscriptionDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageRoleSubscriptionDataResponse from a JSON string
message_role_subscription_data_response_instance = MessageRoleSubscriptionDataResponse.from_json(json)
# print the JSON string representation of the object
print(MessageRoleSubscriptionDataResponse.to_json())

# convert the object into a dict
message_role_subscription_data_response_dict = message_role_subscription_data_response_instance.to_dict()
# create an instance of MessageRoleSubscriptionDataResponse from a dict
message_role_subscription_data_response_from_dict = MessageRoleSubscriptionDataResponse.from_dict(message_role_subscription_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



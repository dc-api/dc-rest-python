# UpdateWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.update_webhook_request import UpdateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookRequest from a JSON string
update_webhook_request_instance = UpdateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookRequest.to_json())

# convert the object into a dict
update_webhook_request_dict = update_webhook_request_instance.to_dict()
# create an instance of UpdateWebhookRequest from a dict
update_webhook_request_from_dict = UpdateWebhookRequest.from_dict(update_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



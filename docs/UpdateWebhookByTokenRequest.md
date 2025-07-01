# UpdateWebhookByTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.update_webhook_by_token_request import UpdateWebhookByTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookByTokenRequest from a JSON string
update_webhook_by_token_request_instance = UpdateWebhookByTokenRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookByTokenRequest.to_json())

# convert the object into a dict
update_webhook_by_token_request_dict = update_webhook_by_token_request_instance.to_dict()
# create an instance of UpdateWebhookByTokenRequest from a dict
update_webhook_by_token_request_from_dict = UpdateWebhookByTokenRequest.from_dict(update_webhook_by_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



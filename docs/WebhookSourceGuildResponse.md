# WebhookSourceGuildResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**icon** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from dc_rest.models.webhook_source_guild_response import WebhookSourceGuildResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSourceGuildResponse from a JSON string
webhook_source_guild_response_instance = WebhookSourceGuildResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookSourceGuildResponse.to_json())

# convert the object into a dict
webhook_source_guild_response_dict = webhook_source_guild_response_instance.to_dict()
# create an instance of WebhookSourceGuildResponse from a dict
webhook_source_guild_response_from_dict = WebhookSourceGuildResponse.from_dict(webhook_source_guild_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



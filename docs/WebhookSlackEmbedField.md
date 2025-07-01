# WebhookSlackEmbedField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**inline** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.webhook_slack_embed_field import WebhookSlackEmbedField

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSlackEmbedField from a JSON string
webhook_slack_embed_field_instance = WebhookSlackEmbedField.from_json(json)
# print the JSON string representation of the object
print(WebhookSlackEmbedField.to_json())

# convert the object into a dict
webhook_slack_embed_field_dict = webhook_slack_embed_field_instance.to_dict()
# create an instance of WebhookSlackEmbedField from a dict
webhook_slack_embed_field_from_dict = WebhookSlackEmbedField.from_dict(webhook_slack_embed_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



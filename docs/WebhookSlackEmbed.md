# WebhookSlackEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**title_link** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**ts** | **int** |  | [optional] 
**pretext** | **str** |  | [optional] 
**footer** | **str** |  | [optional] 
**footer_icon** | **str** |  | [optional] 
**author_name** | **str** |  | [optional] 
**author_link** | **str** |  | [optional] 
**author_icon** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**thumb_url** | **str** |  | [optional] 
**fields** | [**List[WebhookSlackEmbedField]**](WebhookSlackEmbedField.md) |  | [optional] 

## Example

```python
from dc_rest.models.webhook_slack_embed import WebhookSlackEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSlackEmbed from a JSON string
webhook_slack_embed_instance = WebhookSlackEmbed.from_json(json)
# print the JSON string representation of the object
print(WebhookSlackEmbed.to_json())

# convert the object into a dict
webhook_slack_embed_dict = webhook_slack_embed_instance.to_dict()
# create an instance of WebhookSlackEmbed from a dict
webhook_slack_embed_from_dict = WebhookSlackEmbed.from_dict(webhook_slack_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



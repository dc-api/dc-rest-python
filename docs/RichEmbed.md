# RichEmbed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**color** | **int** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**author** | [**RichEmbedAuthor**](RichEmbedAuthor.md) |  | [optional] 
**image** | [**RichEmbedImage**](RichEmbedImage.md) |  | [optional] 
**thumbnail** | [**RichEmbedThumbnail**](RichEmbedThumbnail.md) |  | [optional] 
**footer** | [**RichEmbedFooter**](RichEmbedFooter.md) |  | [optional] 
**fields** | [**List[RichEmbedField]**](RichEmbedField.md) |  | [optional] 
**provider** | [**RichEmbedProvider**](RichEmbedProvider.md) |  | [optional] 
**video** | [**RichEmbedVideo**](RichEmbedVideo.md) |  | [optional] 

## Example

```python
from dc_rest.models.rich_embed import RichEmbed

# TODO update the JSON string below
json = "{}"
# create an instance of RichEmbed from a JSON string
rich_embed_instance = RichEmbed.from_json(json)
# print the JSON string representation of the object
print(RichEmbed.to_json())

# convert the object into a dict
rich_embed_dict = rich_embed_instance.to_dict()
# create an instance of RichEmbed from a dict
rich_embed_from_dict = RichEmbed.from_dict(rich_embed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



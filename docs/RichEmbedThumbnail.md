# RichEmbedThumbnail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**placeholder** | **str** |  | [optional] 
**placeholder_version** | **int** |  | [optional] 
**is_animated** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.rich_embed_thumbnail import RichEmbedThumbnail

# TODO update the JSON string below
json = "{}"
# create an instance of RichEmbedThumbnail from a JSON string
rich_embed_thumbnail_instance = RichEmbedThumbnail.from_json(json)
# print the JSON string representation of the object
print(RichEmbedThumbnail.to_json())

# convert the object into a dict
rich_embed_thumbnail_dict = rich_embed_thumbnail_instance.to_dict()
# create an instance of RichEmbedThumbnail from a dict
rich_embed_thumbnail_from_dict = RichEmbedThumbnail.from_dict(rich_embed_thumbnail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



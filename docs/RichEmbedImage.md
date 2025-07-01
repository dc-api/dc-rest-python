# RichEmbedImage


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
from dc_rest.models.rich_embed_image import RichEmbedImage

# TODO update the JSON string below
json = "{}"
# create an instance of RichEmbedImage from a JSON string
rich_embed_image_instance = RichEmbedImage.from_json(json)
# print the JSON string representation of the object
print(RichEmbedImage.to_json())

# convert the object into a dict
rich_embed_image_dict = rich_embed_image_instance.to_dict()
# create an instance of RichEmbedImage from a dict
rich_embed_image_from_dict = RichEmbedImage.from_dict(rich_embed_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



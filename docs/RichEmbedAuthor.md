# RichEmbedAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.rich_embed_author import RichEmbedAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of RichEmbedAuthor from a JSON string
rich_embed_author_instance = RichEmbedAuthor.from_json(json)
# print the JSON string representation of the object
print(RichEmbedAuthor.to_json())

# convert the object into a dict
rich_embed_author_dict = rich_embed_author_instance.to_dict()
# create an instance of RichEmbedAuthor from a dict
rich_embed_author_from_dict = RichEmbedAuthor.from_dict(rich_embed_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



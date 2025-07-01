# RichEmbedField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 
**inline** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.rich_embed_field import RichEmbedField

# TODO update the JSON string below
json = "{}"
# create an instance of RichEmbedField from a JSON string
rich_embed_field_instance = RichEmbedField.from_json(json)
# print the JSON string representation of the object
print(RichEmbedField.to_json())

# convert the object into a dict
rich_embed_field_dict = rich_embed_field_instance.to_dict()
# create an instance of RichEmbedField from a dict
rich_embed_field_from_dict = RichEmbedField.from_dict(rich_embed_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RichEmbedFooter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.rich_embed_footer import RichEmbedFooter

# TODO update the JSON string below
json = "{}"
# create an instance of RichEmbedFooter from a JSON string
rich_embed_footer_instance = RichEmbedFooter.from_json(json)
# print the JSON string representation of the object
print(RichEmbedFooter.to_json())

# convert the object into a dict
rich_embed_footer_dict = rich_embed_footer_instance.to_dict()
# create an instance of RichEmbedFooter from a dict
rich_embed_footer_from_dict = RichEmbedFooter.from_dict(rich_embed_footer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



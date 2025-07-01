# RichEmbedProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.rich_embed_provider import RichEmbedProvider

# TODO update the JSON string below
json = "{}"
# create an instance of RichEmbedProvider from a JSON string
rich_embed_provider_instance = RichEmbedProvider.from_json(json)
# print the JSON string representation of the object
print(RichEmbedProvider.to_json())

# convert the object into a dict
rich_embed_provider_dict = rich_embed_provider_instance.to_dict()
# create an instance of RichEmbedProvider from a dict
rich_embed_provider_from_dict = RichEmbedProvider.from_dict(rich_embed_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GetSticker200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**tags** | **str** |  | 
**type** | **int** |  | 
**format_type** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**available** | **bool** |  | 
**guild_id** | **str** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 
**pack_id** | **str** |  | 
**sort_value** | **int** |  | 

## Example

```python
from dc_rest.models.get_sticker200_response import GetSticker200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSticker200Response from a JSON string
get_sticker200_response_instance = GetSticker200Response.from_json(json)
# print the JSON string representation of the object
print(GetSticker200Response.to_json())

# convert the object into a dict
get_sticker200_response_dict = get_sticker200_response_instance.to_dict()
# create an instance of GetSticker200Response from a dict
get_sticker200_response_from_dict = GetSticker200Response.from_dict(get_sticker200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



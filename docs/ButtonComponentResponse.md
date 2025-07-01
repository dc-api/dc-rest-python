# ButtonComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**custom_id** | **str** |  | [optional] 
**style** | **int** |  | 
**label** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**emoji** | [**ComponentEmojiResponse**](ComponentEmojiResponse.md) |  | [optional] 
**url** | **str** |  | [optional] 
**sku_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.button_component_response import ButtonComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ButtonComponentResponse from a JSON string
button_component_response_instance = ButtonComponentResponse.from_json(json)
# print the JSON string representation of the object
print(ButtonComponentResponse.to_json())

# convert the object into a dict
button_component_response_dict = button_component_response_instance.to_dict()
# create an instance of ButtonComponentResponse from a dict
button_component_response_from_dict = ButtonComponentResponse.from_dict(button_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



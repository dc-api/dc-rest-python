# ButtonComponentForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**custom_id** | **str** |  | [optional] 
**style** | **int** |  | 
**label** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 
**sku_id** | **str** |  | [optional] 
**emoji** | [**ComponentEmojiForMessageRequest**](ComponentEmojiForMessageRequest.md) |  | [optional] 

## Example

```python
from dc_rest.models.button_component_for_message_request import ButtonComponentForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ButtonComponentForMessageRequest from a JSON string
button_component_for_message_request_instance = ButtonComponentForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(ButtonComponentForMessageRequest.to_json())

# convert the object into a dict
button_component_for_message_request_dict = button_component_for_message_request_instance.to_dict()
# create an instance of ButtonComponentForMessageRequest from a dict
button_component_for_message_request_from_dict = ButtonComponentForMessageRequest.from_dict(button_component_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



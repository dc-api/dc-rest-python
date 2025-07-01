# SectionComponentForMessageRequestAccessory


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
**description** | **str** |  | [optional] 
**spoiler** | **bool** |  | [optional] 
**media** | [**UnfurledMediaRequest**](UnfurledMediaRequest.md) |  | 

## Example

```python
from dc_rest.models.section_component_for_message_request_accessory import SectionComponentForMessageRequestAccessory

# TODO update the JSON string below
json = "{}"
# create an instance of SectionComponentForMessageRequestAccessory from a JSON string
section_component_for_message_request_accessory_instance = SectionComponentForMessageRequestAccessory.from_json(json)
# print the JSON string representation of the object
print(SectionComponentForMessageRequestAccessory.to_json())

# convert the object into a dict
section_component_for_message_request_accessory_dict = section_component_for_message_request_accessory_instance.to_dict()
# create an instance of SectionComponentForMessageRequestAccessory from a dict
section_component_for_message_request_accessory_from_dict = SectionComponentForMessageRequestAccessory.from_dict(section_component_for_message_request_accessory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



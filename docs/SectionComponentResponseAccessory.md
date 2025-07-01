# SectionComponentResponseAccessory


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
**media** | [**UnfurledMediaResponse**](UnfurledMediaResponse.md) |  | 
**description** | **str** |  | [optional] 
**spoiler** | **bool** |  | 

## Example

```python
from dc_rest.models.section_component_response_accessory import SectionComponentResponseAccessory

# TODO update the JSON string below
json = "{}"
# create an instance of SectionComponentResponseAccessory from a JSON string
section_component_response_accessory_instance = SectionComponentResponseAccessory.from_json(json)
# print the JSON string representation of the object
print(SectionComponentResponseAccessory.to_json())

# convert the object into a dict
section_component_response_accessory_dict = section_component_response_accessory_instance.to_dict()
# create an instance of SectionComponentResponseAccessory from a dict
section_component_response_accessory_from_dict = SectionComponentResponseAccessory.from_dict(section_component_response_accessory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



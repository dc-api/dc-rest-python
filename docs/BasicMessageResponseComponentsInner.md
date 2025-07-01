# BasicMessageResponseComponentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**components** | [**List[TextDisplayComponentResponse]**](TextDisplayComponentResponse.md) |  | 
**accent_color** | **int** |  | [optional] 
**spoiler** | **bool** |  | 
**file** | [**UnfurledMediaResponse**](UnfurledMediaResponse.md) |  | 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**items** | [**List[MediaGalleryItemResponse]**](MediaGalleryItemResponse.md) |  | 
**accessory** | [**SectionComponentResponseAccessory**](SectionComponentResponseAccessory.md) |  | 
**spacing** | **int** |  | 
**divider** | **bool** |  | 
**content** | **str** |  | 

## Example

```python
from dc_rest.models.basic_message_response_components_inner import BasicMessageResponseComponentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BasicMessageResponseComponentsInner from a JSON string
basic_message_response_components_inner_instance = BasicMessageResponseComponentsInner.from_json(json)
# print the JSON string representation of the object
print(BasicMessageResponseComponentsInner.to_json())

# convert the object into a dict
basic_message_response_components_inner_dict = basic_message_response_components_inner_instance.to_dict()
# create an instance of BasicMessageResponseComponentsInner from a dict
basic_message_response_components_inner_from_dict = BasicMessageResponseComponentsInner.from_dict(basic_message_response_components_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SectionComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**components** | [**List[TextDisplayComponentResponse]**](TextDisplayComponentResponse.md) |  | 
**accessory** | [**SectionComponentResponseAccessory**](SectionComponentResponseAccessory.md) |  | 

## Example

```python
from dc_rest.models.section_component_response import SectionComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SectionComponentResponse from a JSON string
section_component_response_instance = SectionComponentResponse.from_json(json)
# print the JSON string representation of the object
print(SectionComponentResponse.to_json())

# convert the object into a dict
section_component_response_dict = section_component_response_instance.to_dict()
# create an instance of SectionComponentResponse from a dict
section_component_response_from_dict = SectionComponentResponse.from_dict(section_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



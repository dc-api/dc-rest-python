# SectionComponentForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**components** | [**List[TextDisplayComponentForMessageRequest]**](TextDisplayComponentForMessageRequest.md) |  | 
**accessory** | [**SectionComponentForMessageRequestAccessory**](SectionComponentForMessageRequestAccessory.md) |  | 

## Example

```python
from dc_rest.models.section_component_for_message_request import SectionComponentForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SectionComponentForMessageRequest from a JSON string
section_component_for_message_request_instance = SectionComponentForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(SectionComponentForMessageRequest.to_json())

# convert the object into a dict
section_component_for_message_request_dict = section_component_for_message_request_instance.to_dict()
# create an instance of SectionComponentForMessageRequest from a dict
section_component_for_message_request_from_dict = SectionComponentForMessageRequest.from_dict(section_component_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



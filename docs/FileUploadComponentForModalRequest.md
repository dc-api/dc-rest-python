# FileUploadComponentForModalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | [optional] 
**custom_id** | **str** |  | 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**required** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.file_upload_component_for_modal_request import FileUploadComponentForModalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadComponentForModalRequest from a JSON string
file_upload_component_for_modal_request_instance = FileUploadComponentForModalRequest.from_json(json)
# print the JSON string representation of the object
print(FileUploadComponentForModalRequest.to_json())

# convert the object into a dict
file_upload_component_for_modal_request_dict = file_upload_component_for_modal_request_instance.to_dict()
# create an instance of FileUploadComponentForModalRequest from a dict
file_upload_component_for_modal_request_from_dict = FileUploadComponentForModalRequest.from_dict(file_upload_component_for_modal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



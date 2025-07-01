# CreateThreadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**auto_archive_duration** | **int** |  | [optional] 
**rate_limit_per_user** | **int** |  | [optional] 
**applied_tags** | **List[str]** |  | [optional] 
**message** | [**BaseCreateMessageCreateRequest**](BaseCreateMessageCreateRequest.md) |  | 
**type** | **int** |  | [optional] 
**invitable** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.create_thread_request import CreateThreadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateThreadRequest from a JSON string
create_thread_request_instance = CreateThreadRequest.from_json(json)
# print the JSON string representation of the object
print(CreateThreadRequest.to_json())

# convert the object into a dict
create_thread_request_dict = create_thread_request_instance.to_dict()
# create an instance of CreateThreadRequest from a dict
create_thread_request_from_dict = CreateThreadRequest.from_dict(create_thread_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



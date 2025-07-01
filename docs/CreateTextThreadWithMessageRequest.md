# CreateTextThreadWithMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**auto_archive_duration** | **int** |  | [optional] 
**rate_limit_per_user** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.create_text_thread_with_message_request import CreateTextThreadWithMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTextThreadWithMessageRequest from a JSON string
create_text_thread_with_message_request_instance = CreateTextThreadWithMessageRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTextThreadWithMessageRequest.to_json())

# convert the object into a dict
create_text_thread_with_message_request_dict = create_text_thread_with_message_request_instance.to_dict()
# create an instance of CreateTextThreadWithMessageRequest from a dict
create_text_thread_with_message_request_from_dict = CreateTextThreadWithMessageRequest.from_dict(create_text_thread_with_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



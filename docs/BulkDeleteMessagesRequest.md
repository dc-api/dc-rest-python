# BulkDeleteMessagesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | **List[str]** |  | 

## Example

```python
from dc_rest.models.bulk_delete_messages_request import BulkDeleteMessagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteMessagesRequest from a JSON string
bulk_delete_messages_request_instance = BulkDeleteMessagesRequest.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteMessagesRequest.to_json())

# convert the object into a dict
bulk_delete_messages_request_dict = bulk_delete_messages_request_instance.to_dict()
# create an instance of BulkDeleteMessagesRequest from a dict
bulk_delete_messages_request_from_dict = BulkDeleteMessagesRequest.from_dict(bulk_delete_messages_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



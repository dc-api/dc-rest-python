# MessageSnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**MinimalContentMessageResponse**](MinimalContentMessageResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.message_snapshot_response import MessageSnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageSnapshotResponse from a JSON string
message_snapshot_response_instance = MessageSnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(MessageSnapshotResponse.to_json())

# convert the object into a dict
message_snapshot_response_dict = message_snapshot_response_instance.to_dict()
# create an instance of MessageSnapshotResponse from a dict
message_snapshot_response_from_dict = MessageSnapshotResponse.from_dict(message_snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



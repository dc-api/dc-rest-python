# ExternalScheduledEventCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**scheduled_start_time** | **datetime** |  | 
**scheduled_end_time** | **datetime** |  | [optional] 
**privacy_level** | **object** |  | 
**entity_type** | **int** |  | 
**channel_id** | **str** |  | [optional] 
**entity_metadata** | [**EntityMetadataExternal**](EntityMetadataExternal.md) |  | 

## Example

```python
from dc_rest.models.external_scheduled_event_create_request import ExternalScheduledEventCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalScheduledEventCreateRequest from a JSON string
external_scheduled_event_create_request_instance = ExternalScheduledEventCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalScheduledEventCreateRequest.to_json())

# convert the object into a dict
external_scheduled_event_create_request_dict = external_scheduled_event_create_request_instance.to_dict()
# create an instance of ExternalScheduledEventCreateRequest from a dict
external_scheduled_event_create_request_from_dict = ExternalScheduledEventCreateRequest.from_dict(external_scheduled_event_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



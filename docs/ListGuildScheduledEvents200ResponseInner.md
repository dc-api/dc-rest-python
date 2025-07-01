# ListGuildScheduledEvents200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**guild_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**creator** | [**UserResponse**](UserResponse.md) |  | [optional] 
**image** | **str** |  | [optional] 
**scheduled_start_time** | **datetime** |  | 
**scheduled_end_time** | **datetime** |  | [optional] 
**status** | **int** |  | 
**entity_type** | **int** |  | 
**entity_id** | **str** |  | [optional] 
**user_count** | **int** |  | [optional] 
**privacy_level** | **object** |  | 
**user_rsvp** | [**ScheduledEventUserResponse**](ScheduledEventUserResponse.md) |  | [optional] 
**entity_metadata** | **object** |  | 

## Example

```python
from dc_rest.models.list_guild_scheduled_events200_response_inner import ListGuildScheduledEvents200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListGuildScheduledEvents200ResponseInner from a JSON string
list_guild_scheduled_events200_response_inner_instance = ListGuildScheduledEvents200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListGuildScheduledEvents200ResponseInner.to_json())

# convert the object into a dict
list_guild_scheduled_events200_response_inner_dict = list_guild_scheduled_events200_response_inner_instance.to_dict()
# create an instance of ListGuildScheduledEvents200ResponseInner from a dict
list_guild_scheduled_events200_response_inner_from_dict = ListGuildScheduledEvents200ResponseInner.from_dict(list_guild_scheduled_events200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



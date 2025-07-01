# ScheduledEventUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guild_scheduled_event_id** | **str** |  | 
**user_id** | **str** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 
**member** | [**GuildMemberResponse**](GuildMemberResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.scheduled_event_user_response import ScheduledEventUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledEventUserResponse from a JSON string
scheduled_event_user_response_instance = ScheduledEventUserResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduledEventUserResponse.to_json())

# convert the object into a dict
scheduled_event_user_response_dict = scheduled_event_user_response_instance.to_dict()
# create an instance of ScheduledEventUserResponse from a dict
scheduled_event_user_response_from_dict = ScheduledEventUserResponse.from_dict(scheduled_event_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



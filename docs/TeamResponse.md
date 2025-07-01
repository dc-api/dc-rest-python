# TeamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**icon** | **str** |  | [optional] 
**name** | **str** |  | 
**owner_user_id** | **str** |  | 
**members** | [**List[TeamMemberResponse]**](TeamMemberResponse.md) |  | 

## Example

```python
from dc_rest.models.team_response import TeamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TeamResponse from a JSON string
team_response_instance = TeamResponse.from_json(json)
# print the JSON string representation of the object
print(TeamResponse.to_json())

# convert the object into a dict
team_response_dict = team_response_instance.to_dict()
# create an instance of TeamResponse from a dict
team_response_from_dict = TeamResponse.from_dict(team_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



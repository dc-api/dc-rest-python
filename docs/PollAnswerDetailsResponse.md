# PollAnswerDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UserResponse]**](UserResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.poll_answer_details_response import PollAnswerDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollAnswerDetailsResponse from a JSON string
poll_answer_details_response_instance = PollAnswerDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(PollAnswerDetailsResponse.to_json())

# convert the object into a dict
poll_answer_details_response_dict = poll_answer_details_response_instance.to_dict()
# create an instance of PollAnswerDetailsResponse from a dict
poll_answer_details_response_from_dict = PollAnswerDetailsResponse.from_dict(poll_answer_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



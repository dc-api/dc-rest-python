# PollAnswerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer_id** | **int** |  | 
**poll_media** | [**PollMediaResponse**](PollMediaResponse.md) |  | 

## Example

```python
from dc_rest.models.poll_answer_response import PollAnswerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollAnswerResponse from a JSON string
poll_answer_response_instance = PollAnswerResponse.from_json(json)
# print the JSON string representation of the object
print(PollAnswerResponse.to_json())

# convert the object into a dict
poll_answer_response_dict = poll_answer_response_instance.to_dict()
# create an instance of PollAnswerResponse from a dict
poll_answer_response_from_dict = PollAnswerResponse.from_dict(poll_answer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ActivitiesAttachmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment** | [**AttachmentResponse**](AttachmentResponse.md) |  | 

## Example

```python
from dc_rest.models.activities_attachment_response import ActivitiesAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivitiesAttachmentResponse from a JSON string
activities_attachment_response_instance = ActivitiesAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(ActivitiesAttachmentResponse.to_json())

# convert the object into a dict
activities_attachment_response_dict = activities_attachment_response_instance.to_dict()
# create an instance of ActivitiesAttachmentResponse from a dict
activities_attachment_response_from_dict = ActivitiesAttachmentResponse.from_dict(activities_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GithubReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**GithubUser**](GithubUser.md) |  | 
**body** | **str** |  | [optional] 
**html_url** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from dc_rest.models.github_review import GithubReview

# TODO update the JSON string below
json = "{}"
# create an instance of GithubReview from a JSON string
github_review_instance = GithubReview.from_json(json)
# print the JSON string representation of the object
print(GithubReview.to_json())

# convert the object into a dict
github_review_dict = github_review_instance.to_dict()
# create an instance of GithubReview from a dict
github_review_from_dict = GithubReview.from_dict(github_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



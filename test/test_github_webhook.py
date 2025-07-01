# coding: utf-8

"""
Discord HTTP API (Preview) - REST API Client
Preview of the Discord v10 HTTP API specification. See https://discord.com/developers/docs for more details.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 10
- **Modified**: 2025-07-01T06:33:02.994204459Z[Etc/UTC]
- **Generator Version**: 7.14.0

<details>
<summary><strong>⚠️ Important Disclaimer & Limitation of Liability</strong></summary>
<br>
> **IMPORTANT**: This software is provided "as is" without any warranties, express or implied, including but not limited
> to warranties of merchantability, fitness for a particular purpose, or non-infringement. The developers, contributors,
> and licensors (collectively, "Developers") make no representations regarding the accuracy, completeness, or reliability
> of this software or its outputs.
>
> This client is not intended to provide financial, investment, tax, or legal advice. It facilitates interaction with the
> Discord HTTP API (Preview) service but does not endorse or recommend any financial actions, including the purchase, sale, or holding of
> financial instruments (e.g., stocks, bonds, derivatives, cryptocurrencies). Users must consult qualified financial or
> legal professionals before making decisions based on this software's outputs.
>
> Financial markets are inherently speculative and carry significant risks. Using this software in trading, analysis, or
> other financial activities may result in substantial losses, including total loss of capital. The Developers are not
> liable for any losses or damages arising from such use. Users assume full responsibility for validating the software's
> outputs and ensuring their suitability for intended purposes.
>
> This client may rely on third-party data or services (e.g., market feeds, APIs). The Developers do not control or verify
> the accuracy of these services and are not liable for any errors, delays, or losses resulting from their use. Users must
> comply with third-party terms and conditions.
>
> Users are solely responsible for ensuring compliance with all applicable financial, tax, and regulatory requirements in
> their jurisdiction. This includes obtaining necessary licenses or approvals for trading or investment activities. The
> Developers disclaim liability for any legal consequences arising from non-compliance.
>
> To the fullest extent permitted by law, the Developers shall not be liable for any direct, indirect, incidental,
> consequential, or punitive damages arising from the use or inability to use this software, including but not limited to
> loss of profits, data, or business opportunities.

</details>
"""  # noqa: E501


import unittest

from dc_rest.models.github_webhook import GithubWebhook

class TestGithubWebhook(unittest.TestCase):
    """GithubWebhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GithubWebhook:
        """Test GithubWebhook
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GithubWebhook`
        """
        model = GithubWebhook()
        if include_optional:
            return GithubWebhook(
                action = '',
                ref = '',
                ref_type = '',
                comment = dc_rest.models.github_comment.GithubComment(
                    id = 56, 
                    html_url = '', 
                    user = dc_rest.models.github_user.GithubUser(
                        id = 56, 
                        login = '', 
                        html_url = '', 
                        avatar_url = '', ), 
                    commit_id = '', 
                    body = '', ),
                issue = dc_rest.models.github_issue.GithubIssue(
                    id = 56, 
                    number = 56, 
                    html_url = '', 
                    user = dc_rest.models.github_user.GithubUser(
                        id = 56, 
                        login = '', 
                        html_url = '', 
                        avatar_url = '', ), 
                    title = '', 
                    body = '', 
                    pull_request = null, ),
                pull_request = dc_rest.models.github_issue.GithubIssue(
                    id = 56, 
                    number = 56, 
                    html_url = '', 
                    user = dc_rest.models.github_user.GithubUser(
                        id = 56, 
                        login = '', 
                        html_url = '', 
                        avatar_url = '', ), 
                    title = '', 
                    body = '', 
                    pull_request = null, ),
                repository = dc_rest.models.github_repository.GithubRepository(
                    id = 56, 
                    html_url = '', 
                    name = '', 
                    full_name = '', ),
                forkee = dc_rest.models.github_repository.GithubRepository(
                    id = 56, 
                    html_url = '', 
                    name = '', 
                    full_name = '', ),
                sender = dc_rest.models.github_user.GithubUser(
                    id = 56, 
                    login = '', 
                    html_url = '', 
                    avatar_url = '', ),
                member = dc_rest.models.github_user.GithubUser(
                    id = 56, 
                    login = '', 
                    html_url = '', 
                    avatar_url = '', ),
                release = dc_rest.models.github_release.GithubRelease(
                    id = 56, 
                    tag_name = '', 
                    html_url = '', 
                    author = dc_rest.models.github_user.GithubUser(
                        id = 56, 
                        login = '', 
                        html_url = '', 
                        avatar_url = '', ), ),
                head_commit = dc_rest.models.github_commit.GithubCommit(
                    id = '', 
                    url = '', 
                    message = '', 
                    author = dc_rest.models.github_author.GithubAuthor(
                        username = '', 
                        name = '', ), ),
                commits = [
                    dc_rest.models.github_commit.GithubCommit(
                        id = '', 
                        url = '', 
                        message = '', 
                        author = dc_rest.models.github_author.GithubAuthor(
                            username = '', 
                            name = '', ), )
                    ],
                forced = True,
                compare = '',
                review = dc_rest.models.github_review.GithubReview(
                    user = dc_rest.models.github_user.GithubUser(
                        id = 56, 
                        login = '', 
                        html_url = '', 
                        avatar_url = '', ), 
                    body = '', 
                    html_url = '', 
                    state = '', ),
                check_run = dc_rest.models.github_check_run.GithubCheckRun(
                    conclusion = '', 
                    name = '', 
                    html_url = '', 
                    check_suite = dc_rest.models.github_check_suite.GithubCheckSuite(
                        conclusion = '', 
                        head_branch = '', 
                        head_sha = '', 
                        pull_requests = [
                            dc_rest.models.github_check_pull_request.GithubCheckPullRequest(
                                number = 56, )
                            ], 
                        app = dc_rest.models.github_check_app.GithubCheckApp(
                            name = '', ), ), 
                    details_url = '', 
                    output = dc_rest.models.github_check_run_output.GithubCheckRunOutput(
                        title = '', 
                        summary = '', ), 
                    pull_requests = [
                        dc_rest.models.github_check_pull_request.GithubCheckPullRequest(
                            number = 56, )
                        ], ),
                check_suite = dc_rest.models.github_check_suite.GithubCheckSuite(
                    conclusion = '', 
                    head_branch = '', 
                    head_sha = '', 
                    pull_requests = [
                        dc_rest.models.github_check_pull_request.GithubCheckPullRequest(
                            number = 56, )
                        ], 
                    app = dc_rest.models.github_check_app.GithubCheckApp(
                        name = '', ), ),
                discussion = dc_rest.models.github_discussion.GithubDiscussion(
                    title = '', 
                    number = 56, 
                    html_url = '', 
                    answer_html_url = '', 
                    body = '', 
                    user = dc_rest.models.github_user.GithubUser(
                        id = 56, 
                        login = '', 
                        html_url = '', 
                        avatar_url = '', ), ),
                answer = dc_rest.models.github_comment.GithubComment(
                    id = 56, 
                    html_url = '', 
                    user = dc_rest.models.github_user.GithubUser(
                        id = 56, 
                        login = '', 
                        html_url = '', 
                        avatar_url = '', ), 
                    commit_id = '', 
                    body = '', )
            )
        else:
            return GithubWebhook(
                sender = dc_rest.models.github_user.GithubUser(
                    id = 56, 
                    login = '', 
                    html_url = '', 
                    avatar_url = '', ),
        )
        """

    def testGithubWebhook(self):
        """Test GithubWebhook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

from unittest import TestCase


from Utils.xml_to_dict import get_ispring_only_quiz


# class Test(TestCase):
#     def test_get_ispring_users(self):
#         return
#         s = IspringApi().get_users()
#         users = get_ispring_users(s)
#         print(users)
#
#     def test_get_ispring_enrollment(self):
#         s = IspringApi().get_enrollments()
#         s = '''<?xml version="1.0" encoding="UTF-8"?>
# <response>
#     <enrollment>
#         <enrollmentId>fc1fc35c-040d-11ed-a2ba-b6f58d6fa7b5</enrollmentId>
#         <courseId>1cf62af4-02c3-11ed-8874-3ebfbdfaeb70</courseId>
#         <learnerId>d9261766-040d-11ed-ae50-da994e0c8f89</learnerId>
#         <accessDate>2022-07-14</accessDate>
#         <enrollmentTypeGroup>0</enrollmentTypeGroup>
#         <shouldLockAfterDueDate>0</shouldLockAfterDueDate>
#         <certificate>
#             <issuedCertificateId>66b4ed00-040e-11ed-a8a2-b6f58d6fa7b5</issuedCertificateId>
#             <issueDate>2022-07-15T07:19:00+00:00</issueDate>
#             <expiryDate>2022-07-15T07:21:00+00:00</expiryDate>
#         </certificate>
#     </enrollment>
# </response>'''
#         enrollments = get_ispring_enrollments(s)
#         print(enrollments)
#         s = IspringApi().get_enrollments()
#         enrollments = get_ispring_enrollments(s)
#         print(enrollments)

# def test_get_ispring_contents(self):
#     s = IspringApi().get_content()
#     courses = get_ispring_contents(s)
#     print(courses)



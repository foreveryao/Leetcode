ass Solution(object):
        def intersect(self, nums1, nums2):
            res=[]
            dict1=collection.Count(nums1)
            dict2=collection.Count(nums2)
            both=[i for i in dict1.key() if i in dict2.key()]
            for sub_both in both:
                res.extend([sub_both]*min(dict1[sub_both],dict2[sub_both]))
            return res

class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        clips.sort()
        counter = 0
        left = 0
        right = time
        while left < time:
            max_forward = 0
            for clip in clips:
                if clip[0] <= left:
                    forward = clip[1] - left
                    if forward > max_forward:
                        max_forward = forward
            if max_forward == 0:
                return -1
            left = left + max_forward
            counter += 1
        return counter
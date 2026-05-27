/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), byAscStartTime);

        int currentEndTime = 0;

        for (Interval interval: intervals)
        {
            if (interval.start < currentEndTime)
            {
                return false;
            }

            currentEndTime = interval.end;
        }

        return true;
    }

    static bool byAscStartTime(const Interval& a, const Interval& b)
    {
        return a.start < b.start;
    }
};

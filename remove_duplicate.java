class remove_duplicate {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        int temp[] = new int[n];
        int k=0;
        boolean flag;
        Set<Integer> set = new LinkedHashSet<>();
        for(int i=0;i<n;i++){
            flag=set.add(nums[i]);
            if (flag!=false)
                temp[k++]=nums[i];
        }
        int len = set.size();
        for(int j=0;j<k;j++){
            nums[j]=temp[j];
        }
        // nums=temp;
        return len;
    }
}
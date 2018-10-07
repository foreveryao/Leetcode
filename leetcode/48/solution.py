ass Solution {
        public:
            void rotate(vector<vector<int>>& matrix){
                    int length = matrix.size();
                    for (int i=0;i<length;++i)
                    {
                        for (int j=0;j<length-i;++j)
                        {
                            int tmp=matrix[i][j];
                            matrix[i][j]=matrix[length-j-1][length-i-1];
                            matrix[length-j-1][length-i-1]=tmp;
                        }
                    }

                    for (int i=0;i<length;++i)
                    {
                        for (int j=0;j<length/2;++j)
                        {
                            int tmp=matrix[j][i];
                            matrix[j][i]=matrix[length-j-1][i];
                            matrix[length-j-1][i]=tmp;
                        }
                    }
                }

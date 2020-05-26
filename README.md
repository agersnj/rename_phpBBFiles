# rename_phpBBFiles
when you move or shut down a phpBB Forum, you might need your uploaded files back again

1. get all files from /YOURPATH/www/YOURFORUM/store/oxpus/dlext/downloads

2. find out real_name and file_name from db and save to local file:
  
  SELECT 
    `phpbb3_downloads`.`file_name`,
    `phpbb3_downloads`.`real_file`,
    `phpbb3_downloads`.`file_hash`
  FROM `YOURFORUMDB`.`phpbb3_downloads`;

3. run the Python script in your download directories, with the local fil from your DB sight

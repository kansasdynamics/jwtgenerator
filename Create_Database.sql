-- Create the API database
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'API')
BEGIN
    CREATE DATABASE API;
    PRINT 'Database API created.';
END
ELSE
BEGIN
    PRINT 'Database API already exists.';
END
GO

-- Switch to the API database
USE API;
GO

-- Create the Token table
IF OBJECT_ID('dbo.Token', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Token (
        ID INT PRIMARY KEY,
        JWT NVARCHAR(MAX) NULL,
        LastUpdated DATETIME2 DEFAULT GETUTCDATE()
    );
    PRINT 'Table Token created.';
    
    -- Insert an initial record
    INSERT INTO dbo.Token (ID, JWT)
    VALUES (1, NULL);
    PRINT 'Initial token record inserted.';
END
ELSE
BEGIN
    PRINT 'Table Token already exists.';
END
GO

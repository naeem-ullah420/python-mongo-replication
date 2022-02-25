db
  .getMongo()
  .getDBNames()
  .filter(n => !['admin','local','config'].includes(n))
  .forEach(dname =>
    db
      .getMongo()
      .getDB(dname)
      .dropDatabase()
  )
;
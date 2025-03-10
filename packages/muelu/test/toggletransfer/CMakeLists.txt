
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR})
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/../unit_tests)
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/../../src)
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/../../src/Transfers)
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/../../src/Smoothers)
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/../../gallery)
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/../../adapters/belos)

# first ensure that these cmake boolean variables are defined
ASSERT_DEFINED(
  ${PACKAGE_NAME}_ENABLE_Amesos
  )

ASSERT_DEFINED(
  ${PACKAGE_NAME}_ENABLE_Amesos2
  )



TRIBITS_ADD_EXECUTABLE(
  TogglePFactory_driver
  SOURCES main.cpp
  COMM serial mpi
  )

IF (${PACKAGE_NAME}_ENABLE_Epetra AND ${PACKAGE_NAME}_ENABLE_EpetraExt AND
    ${PACKAGE_NAME}_ENABLE_Ifpack AND ${PACKAGE_NAME}_ENABLE_Amesos)

  MUELU_ADD_SERIAL_AND_MPI_TEST(
    TogglePFactory_driver
    NAME "Driver_TogglePFactory_tent_tent_Epetra"
    ARGS "--matrixType=Laplace3D --nx=40 --ny=40 --nz=60 --mz=1 --xmlFile=parameters_tent_tent.xml --linAlgebra=Epetra"
    NUM_MPI_PROCS 4
    COMM serial mpi
    )

  MUELU_ADD_SERIAL_AND_MPI_TEST(
    TogglePFactory_driver
    NAME "Driver_TogglePFactory_sa_tent_Epetra"
    ARGS "--matrixType=Laplace3D --nx=40 --ny=40 --nz=60 --mz=1 --xmlFile=parameters_sa_tent.xml --linAlgebra=Epetra"
    NUM_MPI_PROCS 4
    COMM serial mpi
    )

  MUELU_ADD_SERIAL_AND_MPI_TEST(
    TogglePFactory_driver
    NAME "Driver_TogglePFactory_semi_tent_Epetra"
    ARGS "--matrixType=Laplace3D --nx=40 --ny=40 --nz=60 --mz=1 --xmlFile=parameters_semi_tent.xml --linAlgebra=Epetra"
    NUM_MPI_PROCS 4
    COMM serial mpi
    )

  TRIBITS_ADD_TEST(
    TogglePFactory_driver
    NAME "Driver_TogglePFactory_semi_tent_line_Epetra"
    ARGS "--matrixType=Laplace3D --nx=40 --ny=40 --nz=60 --mz=1 --xmlFile=parameters_semi_tent_line.xml --linAlgebra=Epetra"
    NUM_MPI_PROCS 4
    COMM serial mpi
    )

  TRIBITS_ADD_TEST(
    TogglePFactory_driver
    NAME "Driver_TogglePFactory_semi_sa_line_easy_Epetra"
    ARGS "--matrixType=Laplace3D --nx=40 --ny=40 --nz=60 --mz=1 --xmlFile=parameters_semi_sa_easy.xml --linAlgebra=Epetra"
    NUM_MPI_PROCS 4
    COMM serial mpi
    )
ENDIF()

IF (${PACKAGE_NAME}_ENABLE_Tpetra AND ${PACKAGE_NAME}_ENABLE_Ifpack2 AND ${PACKAGE_NAME}_ENABLE_Amesos2)
  MUELU_ADD_SERIAL_AND_MPI_TEST(
    TogglePFactory_driver
    NAME "Driver_TogglePFactory_tent_tent_Tpetra"
    ARGS "--matrixType=Laplace3D --nx=40 --ny=40 --nz=60 --mz=1 --xmlFile=parameters_tent_tent.xml --linAlgebra=Tpetra"
    NUM_MPI_PROCS 4
    COMM serial mpi
    )

  MUELU_ADD_SERIAL_AND_MPI_TEST(
    TogglePFactory_driver
    NAME "Driver_TogglePFactory_sa_tent_Tpetra"
    ARGS "--matrixType=Laplace3D --nx=40 --ny=40 --nz=60 --mz=1 --xmlFile=parameters_sa_tent.xml --linAlgebra=Tpetra"
    NUM_MPI_PROCS 4
    COMM serial mpi
    )

  MUELU_ADD_SERIAL_AND_MPI_TEST(
    TogglePFactory_driver
    NAME "Driver_TogglePFactory_semi_tent_Tpetra"
    ARGS "--matrixType=Laplace3D --nx=40 --ny=40 --nz=60 --mz=1 --xmlFile=parameters_semi_tent.xml --linAlgebra=Tpetra"
    NUM_MPI_PROCS 4
    COMM serial mpi
    )

  MUELU_ADD_SERIAL_AND_MPI_TEST(
    TogglePFactory_driver
    NAME "Driver_TogglePFactory_semi_tent_line_Tpetra"
    ARGS "--matrixType=Laplace3D --nx=40 --ny=40 --nz=60 --mz=1 --xmlFile=parameters_semi_tent_line.xml --linAlgebra=Tpetra"
    NUM_MPI_PROCS 4
    COMM serial mpi
    )

  MUELU_ADD_SERIAL_AND_MPI_TEST(
    TogglePFactory_driver
    NAME "Driver_TogglePFactory_semi_sa_line_easy_Tpetra"
    ARGS "--matrixType=Laplace3D --nx=40 --ny=40 --nz=60 --mz=1 --xmlFile=parameters_semi_sa_easy.xml --linAlgebra=Tpetra"
    NUM_MPI_PROCS 4
    COMM serial mpi
    )

  IF (${PACKAGE_NAME}_ENABLE_Kokkos_Refactor)
    MUELU_ADD_SERIAL_AND_MPI_TEST(
      TogglePFactory_driver
      NAME "Driver_TogglePFactory_semi_tent_kokkos_Tpetra"
      ARGS "--matrixType=Laplace3D --nx=40 --ny=40 --nz=60 --mz=1 --xmlFile=parameters_semi_tent_kokkos.xml --linAlgebra=Tpetra"
      NUM_MPI_PROCS 4
      COMM serial mpi
      )
  ENDIF()
ENDIF()

TRIBITS_COPY_FILES_TO_BINARY_DIR(ToggleDriver_cp
  SOURCE_FILES parameters_sa_tent.xml parameters_semi_tent.xml parameters_semi_tent_line.xml parameters_tent_tent.xml parameters_semi_sa_easy.xml parameters_semi_tent_kokkos.xml
  )

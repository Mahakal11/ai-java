module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = "aiops-eks"
  cluster_version = "1.29"

  subnet_ids = ["subnet-xxx", "subnet-yyy"]
  vpc_id     = "vpc-xxx"

  eks_managed_node_groups = {
    default = {
      desired_size = 2
      instance_types = ["t3.medium"]
    }
  }
}
